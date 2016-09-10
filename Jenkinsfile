#!groovy
node {
  step([$class: 'GitHubCommitStatusSetter'])
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
