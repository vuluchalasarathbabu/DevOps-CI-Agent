pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Capture build output into build.log
                bat '''
                    echo Starting build... > build.log
                    echo Compiling source code... >> build.log
                    echo Build completed successfully. >> build.log
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    echo Running tests... >> build.log
                    echo All tests passed. >> build.log
                '''
            }
        }
    }

    post {
        always {
            script {
                // Read full build.log
                def logContent = readFile('build.log')

                // Build JSON payload
                def payload = [
                    buildNumber: env.BUILD_NUMBER,
                    jobName: env.JOB_NAME,
                    status: currentBuild.currentResult,
                    consoleLog: logContent,
                    buildUrl: env.BUILD_URL,
                    gitCommit: env.GIT_COMMIT ?: "N/A"
                ]
                def jsonPayload = groovy.json.JsonOutput.toJson(payload)

                // Write payload to file
                writeFile file: 'payload.json', text: jsonPayload

                // Send POST request using PowerShell (safe step, no approvals needed)
                powershell '''
                    $body = Get-Content payload.json -Raw
                    Invoke-RestMethod -Uri http://localhost:8000/jenkins-webhook `
                                      -Method Post `
                                      -ContentType "application/json" `
                                      -Body $body
                '''
            }

            // Cleanup AFTER sending logs
            cleanWs()
        }
    }
}