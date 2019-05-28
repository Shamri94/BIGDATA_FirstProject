#!/bin/bash

hadoop fs -rm -r /user/output/tmp/tmp_Job3_1M
hadoop fs -rm -r /user/output/Job3_1M
hadoop \
	jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.8.5-amzn-3.jar \
	-D stream.num.map.output.key.fields=3 \
	-D mapreduce.job.reduces=1 \
	-input /user/input/historical_stock_prices_1M.csv \
	-output /user/output/tmp/tmp_Job3_1M \
	-file /home/hadoop/Job_3/historical_stocks.csv \
	-file /home/hadoop/Job_3/mapper1Job3.py \
	-file /home/hadoop/Job_3/reducer1Job3.py \
	-mapper mapper1Job3.py \
	-reducer reducer1Job3.py
hadoop \
	jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.8.5-amzn-3.jar \
	-D stream.num.map.output.key.fields=3 \
	-D mapreduce.job.reduces=1 \
	-input /user/output/tmp/tmp_Job3_1M/part-00000 \
	-output /user/output/Job3_1M \
	-file /home/hadoop/Job_3/mapper2Job3.py \
	-file /home/hadoop/Job_3/reducer2Job3.py \
	-mapper mapper2Job3.py \
	-reducer reducer2Job3.py
