node('Slave-1'){
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
