for i in {1..20}; do
    ($i/run.sh 2>&1 >$i/log) &
done
