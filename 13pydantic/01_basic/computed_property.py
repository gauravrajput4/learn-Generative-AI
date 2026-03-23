from pydantic import BaseModel, computed_field, Field

class Products(BaseModel):
    price:float
    quantity:int

    @computed_field
    @property
    def total_price(self)->float:
        return self.price * self.quantity


class Booking(BaseModel):
    user_id:int
    room_id:int
    nights:int = Field(...,ge=1)
    rate_per_night:float

    @computed_field
    @property
    def total_price(self)->float:
        return self.nights * self.rate_per_night

booking=Booking(
    user_id=123,
    room_id=456,
    nights=2,
    rate_per_night=1000.0
)

print(booking.total_price)
print(booking.model_dump()) # total_price is not included in the output of model_dump() because it's a computed field
