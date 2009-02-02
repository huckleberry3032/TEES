cd ~/cvs_checkout/JariSandbox/ComplexPPI/Source
python SplitAnalysis.py -b MultiEdgeExampleBuilder -x "style:typed,directed,no_linear,entities,maxFeatures" -c SVMMultiClassClassifier -e AveragingMultiClassEvaluator -y "c:10,20,30,40,50,60,70,80,90,100,500,1000,5000,10000,20000,50000,80000,100000,150000,200000,500000,1000000,5000000,10000000;timeout:6000" -i /usr/share/biotext/GeniaChallenge/xml/train.xml -s /usr/share/biotext/GeniaChallenge/xml/devel.xml -o /usr/share/biotext/GeniaChallenge/xml/jari-edges-from-gold-entities -p Charniak-Lease
cd ~/cvs_checkout/GeniaChallenge/triggerRecognition