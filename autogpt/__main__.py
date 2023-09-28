"""Auto-GPT: A GPT powered AI Assistant"""
import autogpt.app.cli

if __name__ == "__main__":
    autogpt.app.cli.main(['--ai-goal', '杭州亚运会，中国几块金牌了', '-c'])
