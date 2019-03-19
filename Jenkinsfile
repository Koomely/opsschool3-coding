node('Slave-1'){
   currentBuild.result = "SUCCESS"
   stage('Printing hello world'){
       sh 'echo "Hello World"'
   }
   stage('Printing runnig_tests'){
       sh 'echo "runnig_tests"'
      sh 'wget https://raw.githubusercontent.com/Koomely/opsschool3-coding/master/home-assignments/session1/excercise1.py'
      sh 'wget https://raw.githubusercontent.com/Koomely/opsschool3-coding/master/home-assignments/session1/sample.json'
      sh 'python3 excercise1.py'
   }
   stage('Printing deploy_to_production'){
       sh 'echo "deploy_to_production"'
   }
}
node('Slave-2'){
   currentBuild.result = "SUCCESS"
   stage('Printing hello world'){
       sh 'echo "Hello World"'
   }
   stage('Printing runnig_tests'){
       sh 'echo "runnig_tests"'
   }
   stage('Printing deploy_to_production'){
       sh 'echo "deploy_to_production"'
   }
}
