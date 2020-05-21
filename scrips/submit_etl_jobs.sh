
pip install -r requirements.txt
spark-submit --master spark://localhost:7077 --deploy-mode client /home/tms/workspace/music-data-analysis/etl/etl.py
