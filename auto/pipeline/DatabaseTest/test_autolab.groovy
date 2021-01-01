// 定义测试场景文件路径变量
// def testplan="./auto/plan/DatabaseTest/test_evcall01.py"

// 声明式 pipeline 替代node
node {
    // init Python 运行环境
    // 初始化一些运行态需要的全局变量
    stage("Init"){
        echo "Init Run Env"
        sh 'python3 --version'
    }

    // 从git获取最新代码
    stage("Check out"){
        echo "check out last code"
        checkout scm
    }

    // 启动测试
    stage("Test"){
        sh "pytest --version"
        dir("."){
            sh "pwd"
            sh "cd ./auto/plan/DatabaseTest/"
            // sh "pytest ${testplan} --html=./logs/report.html --self-contained-html"
            sh "pytest  --html=./logs/report.html --self-contained-html"
            sh "pytest"
        }
    }
    
    // 发布html报告
    stage("Report"){
        dir("."){
            publishHTML(target: [
                alowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'logs',
                reportFiles: 'report.html',
                reportName: "HTML Report"
            ]
            )
        }
    }

    stage("Notify"){
        script{
            if(currentBuild.currentResult == "SUCCESS"){
                // build success,do nothing
                echo "It's build SUCCESS"
                // dingTalk accessToken
            }
            else{
                // build failure or abort send dingTalk
                echo "It's build Faild"

            }
        }
    }
}