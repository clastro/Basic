class Car():

  price_per_raise = 1.0

  def __init__(self, company, details):
    self._company = company
    self._details = details
  
  def __str__(self):
    return 'str : {} - {}'.format(self._company, self._details)
  
  def __repr__(self):
    return 'repr : {} - {}'.format(self._company, self._details)
  
  def detail_info(self):
    print('Current ID : {}'.format(id(self)))
    print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
  
  def get_price(self):
    return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
  
  #Instance Method
  def get_price_culc(self):
    return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise
  
                                                                
  # Class Method
  @classmethod
  def raise_price(cls, per):
    if per <= 1:
      print('Please Enter 1 Or More')
      return
    cls.price_per_raise = per
    print('Succeed! price increased.')
    
Car.price_per_raise = 1.4

Car.raise_price(1.6)



                                                              

                                                              


                                                            
