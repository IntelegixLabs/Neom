# import pybboxes as pbx
#
# voc_bbox = (182, 272, 506, 446)
# W, H = 720, 720  # WxH of the image
# res = pbx.convert_bbox(voc_bbox, from_type="bbox", to_type="yolo", image_size=(W,H))
#
# print(res)


import geocoder
g = geocoder.ip('me')
print(g.latlng)

# import requests
# import json
#
# send_url = "http://api.ipstack.com/check?access_key=YOUR_ACCESS_KEY"
# geo_req = requests.get(send_url)
# geo_json = json.loads(geo_req.text)
# latitude = geo_json['latitude']
# longitude = geo_json['longitude']
# city = geo_json['city']