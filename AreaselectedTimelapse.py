#simple script for making a timelapse using SentinelHub
#forked from https://github.com/sentinel-hub/time-lapse
#and fixed imports that did not work with python 3.5
#Sample video uploaded in youtube https://www.youtube.com/watch?v=uqR8Ice76Rk&feature=youtu.be

import matplotlib.pyplot as plt
import numpy as np
import datetime

from sentinelhub import BBox, CRS
from time_lapse import SentinelHubTimelapse
WMS_INSTANCE = 'YOUR ID HERE'

#define your Area
areaselected = BBox(bbox=[-101.139702,19.734688,-101.070011, 19.696546],
                      crs=CRS.WGS84)

#define the dates to be fetched from SentineHUB.
# nine months create a video of around 2 seconds at 10 fps
time_interval = ['2019-05-01', '2020-01-31']


tl_size = (int(1920/2),int(1080/2))
timelapse=datetime.timedelta(seconds=-1)
areaselected_timelapse = SentinelHubTimelapse('Areaselected',
                                        areaselected,
                                        time_interval,
                                        WMS_INSTANCE,
                                        tl_size)

areaselected_timelapse.get_previews()
areaselected_timelapse.plot_preview(filename='previews.pdf')

areaselected_timelapse.save_fullres_images()
areaselected_timelapse.mask_invalid_images(max_invalid_coverage=0.01)
areaselected_timelapse.mask_cloudy_images(max_cloud_coverage=0.01)
areaselected_timelapse.plot_cloud_masks(filename='cloudmasks.pdf')

areaselected_timelapse.plot_preview(filename='previews_with_cc.pdf')
areaselected_timelapse.make_gif(fps=8, filename='areaselected_8fps.gif')
areaselected_timelapse.make_video(fps=10, filename='areaselected_10fps.avi')
