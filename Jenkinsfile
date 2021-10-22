 pipeline {
    agent {
        dockerfile { args '--user cicd_user'}
    }

    stages {
        stage('Build') {
            options {
                timeout(time: 3, unit: 'MINUTES') 
            }
            steps {
                sh 'poetry build'
            }
        }
        stage('Test') {
            options {
                timeout(time: 5, unit: 'MINUTES') 
            }
            steps {
                sh 'poetry install'
                sh 'poetry run pytest --junitxml=test-report.xml'
            }
            post {
                failure {
                    emailext body: 'Test failure at $BUILD_URL.', recipientProviders: [upstreamDevelopers()], subject: 'Test failure for $JOB_NAME $BUILD_NUMBER', to: 'amuphy9956@live.com', attachmentsPattern: 'test-report.xml'
                }
            }
        }   
    }
    post {
        success {
            junit 'test-report.xml'
            archiveArtifacts 'dist/**.whl'
            emailext body: 'Run succeeded at $BUILD_URL.', recipientProviders: [upstreamDevelopers()], subject: 'Run succeeded for $JOB_NAME $BUILD_NUMBER', to: 'amuphy9956@live.com'

        }
        failure {
            emailext body: 'Run failed at $BUILD_URL, please check the run output.', recipientProviders: [upstreamDevelopers()], subject: 'Run failed for $JOB_NAME $BUILD_NUMBER', to: 'amuphy9956@live.com', attachLog: true
        } 
    }
}