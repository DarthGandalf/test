#!groovy
node {
  step([$class: 'GitHubSetCommitStatusBuilder', statusMessage: [content: 'Hello world']])
  stage('My New Stage') {
    timestamps {
      sh 'echo hello'
      sh 'uname -a'
      sh 'pwd'
      sh 'ls -l'
      sh 'env'
    }
  }
  step([$class: 'GitHubCommitStatusSetter', errorHandlers: [[$class: 'ChangingBuildStatusErrorHandler', result: 'FAILURE']], statusResultSource: [$class: 'ConditionalStatusResultSource', results: []]])
}
