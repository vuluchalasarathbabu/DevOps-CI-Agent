pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat '''
                    echo Building the application... > build.log
                    REM Add your actual build commands here
                '''
            }
        }
    }

    post {
        always {
            script {
                def logContent = readFile('build.log')
                def jsonPayload = groovy.json.JsonOutput.toJson([
                    buildNumber: env.BUILD_NUMBER,
                    jobName: env.JOB_NAME,
                    status: currentBuild.currentResult,
                    consoleLog: logContent
                ])

                // Use PowerShell to send POST request safely
                writeFile file: 'payload.json', text: jsonPayload
                powershell '''
                    $body = Get-Content payload.json -Raw
                    Invoke-RestMethod -Uri http://localhost:8000/jenkins-webhook `
                                      -Method Post `
                                      -ContentType "application/json" `
                                      -Body $body
                '''
            }
        }
    }
}
