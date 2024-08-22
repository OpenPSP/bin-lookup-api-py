from pydantic import BaseModel

class Country(BaseModel):
    Code: str
    Alpha3: str
    Name: str

class Currency(BaseModel):
    Code: str
    Alpha3: str
    Name: str

class Issuer(BaseModel):
    Code: str
    Name: str
    Type: str

class BinResponse(BaseModel):
    BIN: int
    LowAccountRange: int
    HighAccountRange: int
    Brand: str
    CardName: str
    CardDescription: str
    Country: Country
    Region: str
    FundingSource: str
    CheckDigit: bool
    UsageScope: str
    Group: str
    BINPrefix: str
    ICA: str
    ChipTechnology: bool
    Prepaid: bool
    Currency: Currency
    CardType: str
    Contactless: str
    Token: bool
    Issuer: Issuer
