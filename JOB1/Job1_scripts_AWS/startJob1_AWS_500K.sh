#!/bin/bash

hadoop fs -rm -r /user/output/Job1_500K
hadoop \
	jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.8.5-amzn-3.jar \
	-D stream.num.map.output.key.fields=2 \
	-D mapreduce.job.reduces=1 \
	-input /user/input/historical_stock_prices_500K.csv \
	-output /user/output/Job1_500K \
	-file /home/hadoop/Job_1/mapperJob1.py \
	-file /home/hadoop/Job_1/reducerJob1.py \
	-mapper mapperJob1.py \
	-reducer reducerJob1.py
