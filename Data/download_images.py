from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["GRAFFITI", "FADED SIGNAGE", "POTHOLES", "GARBAGE", "CONSTRUCTION ROAD", "BROKEN_SIGNAGE", "BAD STREETLIGHT",
            "BAD BILLBOARD", "SAND ON ROAD", "CLUTTER_SIDEWALK", "UNKEPT_FACADE"]

for kw in keywords:
    response().download(kw, 1000)
