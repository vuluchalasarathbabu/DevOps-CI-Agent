pipeline {
    agent any

    stages {
        // ...existing code...
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Add build steps here if necessary
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'npm install'
                sh 'npm test'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Add deployment steps here if necessary
            }
        }
        // ...existing code...
    }

    // added post section to run steps after pipeline completion
    post {
        success {
            echo 'Pipeline succeeded — running post-success steps...'
            // e.g., notify success, archive artifacts
            // sh 'scripts/success.sh'
        }
        failure {
            echo 'Pipeline failed — running post-failure steps...'
            // e.g., collect logs, notify on failure
            // sh 'scripts/failure.sh'
        }
        always {
            echo 'Always run cleanup steps...'
            // e.g., cleanup workspace
            cleanWs()
        }
    }
}