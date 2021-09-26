import depthai
pipeline = depthai.Pipeline()

# Create nodes, configure them and link them together

# Upload the pipeline to the device
with depthai.Device(pipeline) as device:
  # Start the pipeline that is now on the device
  device.startPipeline()

  # Input queue, to send message from the host to the device (you can recieve the message on the device with XLinkIn)
  input_q = device.getInputQueue("input_name", maxSize=4, blocking=False)

  # Output queue, to recieve message on the host from the device (you can send the message on the device with XLinkOut)
  output_q = device.getOutputQueue("output_name", maxSize=4, blocking=False)

  while True:
      # Get the message from the queue
      output_q.get() # Or output_q.tryGet() for non-blocking

      # Send a message to the device
      cfg = depthai.ImageManipConfig()
      input_q.send(cfg)