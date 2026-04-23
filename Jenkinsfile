pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // On Windows, use bat instead of sh
                bat '''
                    echo Building the application... > build.log
                    REM Add your actual build commands here
                    REM Example: mvn clean install >> build.log
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
            echo 'Sending logs to FastAPI receiver...'
            script {
                // Ensure build.log exists before reading
                if (fileExists('build.log')) {
                    def logContent = readFile('build.log')

                    def payload = [
                        buildNumber: env.BUILD_NUMBER,
                        jobName: env.JOB_NAME,
                        status: currentBuild.currentResult,
                        consoleLog: logContent,
                        buildUrl: env.BUILD_URL,
                        gitCommit: env.GIT_COMMIT ?: "N/A"
                    ]
                    def jsonPayload = groovy.json.JsonOutput.toJson(payload)

                    def response = httpRequest(
                        httpMode: 'POST',
                        contentType: 'APPLICATION_JSON',
                        requestBody: jsonPayload,
                        url: 'http://localhost:8000/jenkins-webhook'
                    )
                    echo "Webhook response: ${response.status}"
                } else {
                    echo "No build.log file found — skipping webhook."
                }
            }

            // Cleanup AFTER sending logs
            cleanWs()
        }
    }
}
