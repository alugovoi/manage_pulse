
import pulsectl
from pulse import pulse

def test_pulse_volume_inc():

  opulse = pulsectl.Pulse()
  sink = opulse.sink_list()[0]
  orig_volume = round(sink.volume.values[0],2)

  pulse.manage_volume(0.01)
  sink = opulse.sink_list()[0]
  assert orig_volume + 0.01 == round(sink.volume.values[0],2)



