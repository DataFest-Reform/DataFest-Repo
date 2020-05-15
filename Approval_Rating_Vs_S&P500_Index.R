# Import the excel data into R
  
  library(readxl)
  StockMarketData2020 <- read_excel("StockMarketData2020.xlsx", 
                                    sheet = "StockVsApprovalRating", 
                                    range = "B1:C122")
  View(StockMarketData2020)

# Generate a scatterplot comparing approval rating vs. stock market
  
  plot(StockMarketData2020$`S&P 500`, 
       StockMarketData2020$`Approval Rating`, 
       xlab = "S&P 500 Index ($)", 
       ylab = "Trump's Approval Rating (%)", 
       main = "Trump's Approval Rating vs. S&P 500 Index", 
       )

# Generate correlation coefficient
  
  cor(StockMarketData2020$`S&P 500`, StockMarketData2020$`Approval Rating`)

# Generate linear regression model
  
  linear_mod <- lm(StockMarketData2020$`Approval Rating` ~ StockMarketData2020$`S&P 500`, StockMarketData2020)
  summary(linear_mod)
  abline(76.096034, -0.012788)
  
 