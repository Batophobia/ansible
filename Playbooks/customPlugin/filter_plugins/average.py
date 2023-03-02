def average(list):
  return sum(list) / float(len(list))

class FilterModule(object):
  def filters(self):
    return {
      # Filter names mapped to functions
      'average': average
    }