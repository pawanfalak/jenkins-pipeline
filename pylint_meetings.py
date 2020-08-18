from pylint.lint import Run

results = Run(['meetings.py'], do_exit=False)
print(results.linter.stats['global_note'])