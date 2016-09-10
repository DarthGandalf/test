#!groovy
node {
  step([$class: 'GitHubCommitStatusSetter', errorHandlers: [[$class: 'ChangingBuildStatusErrorHandler', result: 'FAILURE']]])
  stage('My New Stage') {
    timestamps {
      sh 'echo hello'
      sh 'uname -a'
      sh 'pwd'
      checkout scm
      sh 'ls -l'
    }
  }
}
