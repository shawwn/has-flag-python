from has_flag import has_flag


def test_has_flag():
	assert has_flag('unicorn', ['--foo', '--unicorn', '--bar'])
	assert has_flag('--unicorn', ['--foo', '--unicorn', '--bar']), 'optional prefix'
	assert has_flag('unicorn=rainbow', ['--foo', '--unicorn=rainbow', '--bar'])
	assert has_flag('unicorn', ['--unicorn', '--', '--foo'])
	assert not has_flag('unicorn', ['--foo', '--', '--unicorn']), 'don\'t match flags after terminator'
	assert not has_flag('unicorn', ['--foo'])
	assert has_flag('-u', ['-f', '-u', '-b'])
	assert has_flag('-u', ['-u', '--', '-f'])
	assert has_flag('u', ['-f', '-u', '-b'])
	assert has_flag('u', ['-u', '--', '-f'])
	assert not has_flag('f', ['-u', '--', '-f'])
