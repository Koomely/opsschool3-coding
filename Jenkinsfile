node('Slave-1'){
   currentBuild.result = "SUCCESS"
   stage('Printing hello world'){
       sh 'echo "Hello World"'
   }
   stage('Printing runnig_tests'){
       sh 'echo "runnig_tests"'
      python https://github.com/Koomely/opsschool3-coding.git/home-assignments/session1/excercise1.py
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
      sh 'exit 1'
   }
   stage('Printing deploy_to_production'){
       sh 'echo "deploy_to_production"'
   }
}
