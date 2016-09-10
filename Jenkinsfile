node {
  step([$class: 'GitHubSetCommitStatusBuilder', statusMessage: [content: 'Hello world']])
  stage('My New Stage') {
    sh 'echo hello'
    sh 'uname -a'
    sh 'pwd'
    sh 'ls -l'
  }
  step([$class: 'GitHubCommitStatusSetter', errorHandlers: [[$class: 'ChangingBuildStatusErrorHandler', result: 'FAILURE']], statusResultSource: [$class: 'ConditionalStatusResultSource', results: []]])
}
