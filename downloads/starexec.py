#!/usr/bin/env python3

import argparse
import itertools
import pandas as pd


class StarExecCheckerPipeline:

    def __init__(self, check_model = 737760, check_proof_pre = 737767, check_proof_post = 737762):
        self.check_model = check_model
        self.check_proof_pre = check_proof_pre
        self.check_proof_post = check_proof_post


# address of SAT Pipeline: https://www.starexec.org/starexec/secure/details/solver.jsp?id=33243
class StarExecJob:

    ## Constructor
    # @param name Name of the job as it will appear in the StarExec Job Queue
    # @param global_timeout Global timeout for the complete job pipeline including solvers and checkers (in seconds)
    # @param cpu_timeout CPU timeout for the solver (in seconds)
    # @param wallclock_timeout Wallclock timeout for the solver (in seconds)
    # @param memout Memory limit for the solver (in MB)
    def __init__(self, 
        name: str, 
        #queue_id: int = 186899, # SAT Comp. 2023
        #queue_id: int = 88797, # long.q
        queue_id: int = 1, # all.q
        global_timeout: int = 1800, 
        cpu_timeout: int = 600, 
        wallclock_timeout: int = 1200, 
        memout: int = 128, 
        pipeline: StarExecCheckerPipeline = StarExecCheckerPipeline()
    ):
        self.name = name
        self.queue_id = queue_id
        self.global_timeout = global_timeout
        self.cpu_timeout = cpu_timeout
        self.wallclock_timeout = wallclock_timeout
        self.memout = memout
        self.pipeline = pipeline


    def print_header(self):
        print('<?xml version="1.0" encoding="UTF-8"?>')
        print('<tns:Jobs xmlns:tns="https://www.starexec.org/starexec/public/batchJobSchema.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="https://www.starexec.org/starexec/public/batchJobSchema.xsd batchJobSchema.xsd">')

    ## Specify job pipline for given solver
    # @param config_id ID of the solver run-script in StarExec
    def announce_solver_and_checkers(self, cid_solver):
        cid_extract = 737758
        print("<SolverPipeline name='pipe{}'>".format(cid_solver))
        print("<PipelineStage config-id='{}' primary='true'><BenchmarkDependency input='1'/></PipelineStage>".format(cid_extract))
        print("<PipelineStage config-id='{}'></PipelineStage>".format(cid_solver))
        print("<PipelineStage config-id='{}'><StageDependency stage='1'/></PipelineStage>".format(self.pipeline.check_model))
        print("<PipelineStage config-id='{}'><StageDependency stage='1'/></PipelineStage>".format(self.pipeline.check_proof_pre))
        print("<PipelineStage config-id='{}'><StageDependency stage='1'/></PipelineStage>".format(self.pipeline.check_proof_post))
        print("</SolverPipeline>")


    ## Specify job pipline attributes
    def define_job(self): 
        print("<Job name='{}'><JobAttributes><description value='Proof Checker and Queue Job'/>".format(self.name))
        print("<queue-id value='{}'/>".format(self.queue_id))
        print("<cpu-timeout value='{}'/>".format(self.global_timeout))
        print("<wallclock-timeout value='{}'/>".format(self.global_timeout))
        print("<mem-limit value='{}'/>".format(self.memout))
        print('<bench-framework value="runsolver"/><suppress-timestamps value="true"/></JobAttributes>')
        print('<StageAttributes><stage-num value="1"/>')
        print('<stdout-save value="NoSave"/>')
        print('<other-save value="NoSave"/>')
        print('<postproc-id value="702"/>') # starexec_result = gbdhash
        print('</StageAttributes>')
        print('<StageAttributes><stage-num value="2"/>')
        print("<cpu-timeout value='{}'/><wallclock-timeout value='{}'/>".format(self.cpu_timeout, self.wallclock_timeout))
        print('<other-save value="NoSave"/><postproc-id value="32"/>') # starexec_result = solver result
        print('</StageAttributes>')
        print('<StageAttributes><stage-num value="3"/><other-save value="NoSave"/><postproc-id value="659"/></StageAttributes>') # starexec_result = checkmodel
        print('<StageAttributes><stage-num value="4"/><other-save value="NoSave"/><postproc-id value="266"/></StageAttributes>') # starexec_result = checkproof1
        print('<StageAttributes><stage-num value="5"/><other-save value="NoSave"/><postproc-id value="266"/></StageAttributes>') # starexec_result = checkproof2


    def emit_job(self, config_id, bench_id):
        print("<JobLine pipe-name='pipe{s}' job-space-path='sat' bench-id='{b}'><BenchmarkInput bench-id='{b}'/></JobLine>".format(s=config_id, b=bench_id))


    def print_footer(self):
        print('</Job>')
        print('</tns:Jobs>')


    def generate(self, df: pd.DataFrame):
        self.print_header()
        for config in df['configuration id'].unique():
            self.announce_solver_and_checkers(config)
        self.define_job()
        for index, row in df.iterrows():
            self.emit_job(row['configuration id'], row['benchmark id'])
        self.print_footer()


def main():
    cid_checkmodel = 737760

    cid_drat_trim = 737767
    cid_drat_trim_bin = 737769
    cid_dpr_trim = 737765
    cid_dpr_trim_bin = 737764
    cid_cake_lpr = 737762

    cid_gratgen = 737766
    cid_gratgen_bin = 737759
    cid_gratchk = 737768

    cid_veripb = 737761
    cid_cakepb = 737770

    drat = StarExecCheckerPipeline(cid_checkmodel, cid_drat_trim, cid_cake_lpr)
    dratbin = StarExecCheckerPipeline(cid_checkmodel, cid_drat_trim_bin, cid_cake_lpr)
    dpr = StarExecCheckerPipeline(cid_checkmodel, cid_dpr_trim, cid_cake_lpr)
    dprbin = StarExecCheckerPipeline(cid_checkmodel, cid_dpr_trim_bin, cid_cake_lpr)
    grat = StarExecCheckerPipeline(cid_checkmodel, cid_gratgen, cid_gratchk)
    gratbin = StarExecCheckerPipeline(cid_checkmodel, cid_gratgen_bin, cid_gratchk)
    veripb = StarExecCheckerPipeline(cid_checkmodel, cid_veripb, cid_cakepb)

    parser = argparse.ArgumentParser(description='Generate StarExec job XML')

    parser.add_argument("name", help="Name of the job")

    parser.add_argument("-p", "--pipeline", help="Pipeline to use", choices=['drat', 'dratbin', 'dpr', 'dprbin', 'grat', 'gratbin', 'veripb'], default='drat')

    parser.add_argument("-c", "--csv", help="CSV file with columns 'benchmark id' and 'configuration id'")

    parser.add_argument("-s", "--solvers", help="Solver Configuration IDs", nargs='*', default=[])
    parser.add_argument("-b", "--benchmarks", help="Benchmark IDs", nargs='*', default=[])

    args = parser.parse_args()

    if args.csv and (args.solvers or args.benchmarks):
        parser.error("Cannot use --csv and --solvers/--benchmarks at the same time")
    elif not args.csv and (not args.solvers or not args.benchmarks):
        parser.error("Must use either --csv or --solvers/--benchmarks")

    if args.csv:
        df = pd.read_csv(args.csv)
    else:
        df = pd.DataFrame(list(itertools.product(args.solvers, args.benchmarks)), columns=['configuration id', 'benchmark id'])

    pipeline = drat

    if args.pipeline == 'dratbin':
        pipeline = dratbin
    elif args.pipeline == 'dpr':
        pipeline = dpr
    elif args.pipeline == 'dprbin':
        pipeline = dprbin
    elif args.pipeline == 'grat':
        pipeline = grat
    elif args.pipeline == 'gratbin':
        pipeline = gratbin
    elif args.pipeline == 'veripb':
        pipeline = veripb


    generator = StarExecJob(args.name, pipeline = pipeline)
    generator.generate(df)


if __name__ == '__main__':
    main()


