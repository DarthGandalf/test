#!groovy
node {
  step([$class: 'GitHubCommitStatusSetter', errorHandlers: [[$class: 'ChangingBuildStatusErrorHandler', result: 'FAILURE']], statusResultSource: [$class: 'ConditionalStatusResultSource', results: [[$class: 'BetterThanOrEqualBuildResult', message: '', result: 'SUCCESS', state: 'SUCCESS']]]])
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
