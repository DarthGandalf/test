#!groovy
node {
  timestamps {
    step([$class: 'GitHubCommitStatusSetter'])
    try {
      stage('Allocate') {}
      stage('Build') {
        sh 'echo hello'
        sh 'uname -a'
        sh 'pwd'
        checkout scm
        sh 'ls -l'
        sh 'true'
        sh 'echo bye'
      }
      currentBuild.result = 'SUCCESS'
    } catch (err) {
      echo "Caught: ${err}"
      currentBuild.result = 'FAILURE'
    }
    step([$class: 'GitHubCommitStatusSetter'])
  }
}
