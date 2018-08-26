import pytest

from pulse import cli

def test_cli():
  '''
      the manage_pulse cli should not be executed with multiply cli options (--inc/--dec/--dock/--undock)
  '''
  with pytest.raises(SystemExit):
    parser=cli.create_parser()
    parser.parse_args(['--inc','--dock'])
  with pytest.raises(SystemExit):
    parser=cli.create_parser()
    parser.parse_args(['--undock','--dock'])

def test_inc_option():
  '''
     should fail if --inc has no option
  '''
  with pytest.raises(SystemExit):
    parser=cli.create_parser()
    parser.parse_args(['--inc'])

def test_dock_option():
  '''
     should fail if --dock has option
  '''
  with pytest.raises(SystemExit):
    parser=cli.create_parser()
    parser.parse_args(['--dock','10'])


def test_inc_float_option():
  '''
     inc should be less than 0.5
  '''
  with pytest.raises(SystemExit):
    parser=cli.create_parser()
    parser.parse_args(['--inc','1'])

def test_hp():
  '''
    happy path testing with correct input
  '''
  parser=cli.create_parser()
  args=parser.parse_args(['--dec', '0.3'])
  print args
  assert args.dec == 0.3 
