pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Capture build output into build.log
                sh '''
                    echo "Building the application..." | tee build.log
                    # Add your actual build commands here
                    # Example: mvn clean install | tee -a build.log
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded — running post-success steps...'
            // e.g., notify success, archive artifacts
        }
        failure {
            echo 'Pipeline failed — running post-failure steps...'
            // e.g., collect logs, notify on failure
        }
        always {
            echo 'Always run cleanup steps...'
            cleanWs()

            script {
                // Read captured logs from build.log
                def logContent = readFile('build.log')

                // Build JSON payload
                def payload = [
                    buildNumber: env.BUILD_NUMBER,
                    jobName: env.JOB_NAME,
                    status: currentBuild.currentResult,
                    consoleLog: logContent
                ]
                def jsonPayload = groovy.json.JsonOutput.toJson(payload)

                // Send HTTP POST to FastAPI receiver
                def response = httpRequest(
                    httpMode: 'POST',
                    contentType: 'APPLICATION_JSON',
                    requestBody: jsonPayload,
                    url: 'http://localhost:8000/jenkins-webhook'
                )
                echo "Webhook response: ${response.status}"
            }
        }
    }
}
