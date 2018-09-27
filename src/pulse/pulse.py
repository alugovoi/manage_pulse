
import pulsectl
import time 



def manage_volume(vlm_dff):
  pulse = pulsectl.Pulse()
  sinks = pulse.sink_list()
  for sink in sinks:
    print sink
    pulse.volume_change_all_chans(sink,vlm_dff)
    
def manage_docking(dock_mode):
  DOCK_HEADPHONE_DESC="Headset H390 Analog Stereo"
  DEFAULT_HEADPHONE_DESC="Built-in Audio Analog Stereo"
 
  DEFAULT_MIC_DESC="Built-in Audio Analog Stereo"
  DOCK_MIC_DESC="Headset H390 Analog Mono"

  time.sleep(5)
  pulse = pulsectl.Pulse()
  sinks = pulse.sink_list()
  inputs = pulse.sink_input_list()
  sources = pulse.source_list()

  if dock_mode=='dock':
    dock_sink=[sink for sink in sinks if DOCK_HEADPHONE_DESC in sink.description][0]
    default_sink=[sink for sink in sinks if DEFAULT_HEADPHONE_DESC in sink.description][0]
    default_source=[source for source in sources if DEFAULT_MIC_DESC==source.description][0]
    dock_source=[source for source in sources if DOCK_MIC_DESC==source.description][0]
    pulse.sink_mute(default_sink.index)
    pulse.sink_default_set(dock_sink)

    pulse.source_mute(default_source.index)
    pulse.source_default_set(dock_source)
    for input in inputs:
      pulse.sink_input_move(input.index,dock_sink.index)
  if dock_mode=='undock':
    default_sink=[sink for sink in sinks if DEFAULT_HEADPHONE_DESC in sink.description][0]
    default_source=[source for source in sources if DEFAULT_MIC_DESC==source.description][0]
    pulse.sink_mute(default_sink.index,mute=False)
    pulse.sink_default_set(default_sink)

    pulse.source_mute(default_source.index,mute=False)
    for input in inputs:
      pulse.sink_input_move(input.index,default_sink.index)

  
