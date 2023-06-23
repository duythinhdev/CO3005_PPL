javac .\y.java
javac .\X.java
java -jar .\classfileanalyzer.jar -nopc .\X.class
java -jar .\classfileanalyzer.jar -file .\X.class