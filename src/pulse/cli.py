
import argparse
import sys

class VolumeAction(argparse.Action):
  def __call__(self, parser, namespace, values, option_string=None):
    diff_value = values
    if diff_value>0.5:
      print "the inc/dec value should be less than 0.5"
      sys.exit(2)
    if option_string=="--dec":
      namespace.dec=diff_value
    if option_string=="--inc":
      namespace.inc=diff_value
    
    

def create_parser():
  parser = argparse.ArgumentParser()
  group = parser.add_mutually_exclusive_group()
  
  group.add_argument("--inc",type=float,action=VolumeAction)
  group.add_argument("--dec",type=float,action=VolumeAction)
  group.add_argument("--dock",action="store_true")
  group.add_argument("--undock",action="store_true")
  args = parser.parse_args()

  return parser


def main():
  import pulse as mpulse 
  args = create_parser().parse_args()
  if args.inc:
    mpulse.manage_volume(args.inc)
  if args.dec:
    mpulse.manage_volume(-args.dec)
  if args.dock:
    mpulse.manage_docking("dock")
  if args.undock:
    mpulse.manage_docking("undock")
