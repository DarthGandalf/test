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
      timeout(time:5, unit:'SECONDS') {
        sh 'sleep 10'
      }
      sh 'echo bye'
    }
  }
  step([$class: 'GitHubCommitStatusSetter'])
}
