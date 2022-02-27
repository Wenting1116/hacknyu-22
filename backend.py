import matplotlib
from pip import main
lottery_prize = 120
max_willingness = 0
prob = 0.0
income = 0

z = lottery_prize
lamb = max_willingness  # can't use lambda because it's python keyword
alpha = prob
# calculate rel_risk_aversion
rel_risk_aversion = (alpha * z - lamb) / (lamb**2 / 2 +
                                          alpha * z**2 / 2 - alpha * lamb * z)
pho = rel_risk_aversion
# gradient of relative risk aversion in terms of max willingness to pay
grad_pho_over_lamb = -(pho/(alpha*z-lamb)+pho**2)

# relative risk premium
c = 0.00125 * pho * income
