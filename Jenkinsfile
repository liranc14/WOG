node {
    stage("clone"){
        git branch: 'main', url: 'https://github.com/liranc14/WOG.git'
    }
    stage("execute"){
        sh "ls -l"
        sh "/home/e186601/DevOps2702/.venv_devops/bin/python test.py"
    }
}
