from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic.base import View

import datetime
from BdFinance.utils import render_to_pdf

class PDFgenerate(View):
    def get(self,request,*args,**kwargs):
        pdf = render_to_pdf('invoice.html')
        return HttpResponse(pdf,content_type="application/pdf")

def getPdf( request, *args, **kwargs):
        data = {
             'today': datetime.date.today(),
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('invoice.html', data)
        print(pdf)
        return HttpResponse(pdf, content_type='application/pdf')

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        template = get_template('invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        pdf = render_to_pdf('invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
def homepage(request):
    return render(request,'base.html',{})

def table(request):

    ref= request.POST['ref']
    date= request.POST['date']

    borrower= request.POST['borrower']
    group= request.POST['group']
    sector= request.POST['sector']
    financial= request.POST['financial']
    completedby= request.POST['completedby']
    approvedby= request.POST['approvedby']

    # getting details end

    debt = request.POST['debt1']
    Debt=debt
    debt=float(debt)
    if (debt>2.75):
        debt=0
    elif(debt>2.5 and debt <=2.75):
        debt=7
    elif(debt>2.0 and debt <=2.5):
        debt=8
    elif(debt>1.25 and debt <=2.0):
        debt=10
    elif(debt>0.75 and debt <=1.25):
        debt=11
    elif(debt>0.5 and debt<=0.75):
        debt=12
    elif(debt>0.35 and debt<=0.5):
        debt = 13
    elif(debt>0.25 and debt<=0.35):
        debt=14
    else:
        debt=15


    cur_rat=request.POST['cur_rat']
    Cur_rat=cur_rat
    cur_rat = float(cur_rat)
    if (cur_rat > 2.74):
        cur_rat = 15
    elif (cur_rat > 2.49 and cur_rat <= 2.74):
        cur_rat = 14
    elif (cur_rat > 1.99 and cur_rat <= 2.49):
        cur_rat = 13
    elif (cur_rat > 1.49 and cur_rat <= 1.99):
        cur_rat = 12
    elif (cur_rat > 1.09 and cur_rat <= 1.49):
        cur_rat = 11
    elif (cur_rat > 0.89 and cur_rat <= 1.09):
        cur_rat = 10
    elif (cur_rat > 0.79 and cur_rat <= 0.89):
        cur_rat = 8
    elif (cur_rat > 0.69 and cur_rat <= 0.79):
        cur_rat = 7
    else:
        cur_rat = 0


    opm = request.POST['opm']

    Opm=opm
    opm=opm.strip('%')
    opm = int(float(opm))
    if (opm >=25):
        opm = 15
    elif (opm >=20 and opm < 25):
        opm = 14
    elif (opm >=15 and opm <20):
        opm = 13
    elif (opm >=10 and opm <15):
        opm = 12
    elif (opm >=7 and opm < 10):
        opm = 10
    elif (opm >=4 and opm <7):
        opm = 9
    elif (opm >=1 and opm <4):
        opm = 7

    else:
        opm = 0

    icr = request.POST['icr']
    Icr=icr
    icr=float(icr)
    if (icr >=2.0):
        icr = 5
    elif (icr >=1.5 and icr < 2.0):
        icr = 4
    elif (icr >=1.25 and icr <1.5):
        icr = 3
    elif (icr >=1.0 and icr <1.25):
        icr = 2
    else:
        icr = 0

    totalA=debt+cur_rat+opm+icr
############### End of the first A ##################

    sales= request.POST['sales']
    Sales=sales
    sales=float(sales)
    if(sales>=60):
        sales=5
    elif(sales>=30 and sales <60):
        sales=4
    elif(sales>=10 and sales<30):
        sales=3
    elif(sales>=5 and sales<10):
        sales=2
    elif(sales>2.5 and sales<5):
        sales=1
    else:
        sales=0

    outlook=request.POST['OutLook']
    if(outlook == '1'):
        outlook=1
        Outlook='Slightly Uncertain'
    elif(outlook == '2'):
        outlook=2
        Outlook='Stable'
    elif(outlook == '3'):
        outlook=3
        Outlook='Favourable'
    else:
        outlook=0
        Outlook='Cause for Concern'

    ind_grow=request.POST['ind_grow']
    # print(type(ind_grow))
    # print(ind_grow)
    if(ind_grow =='1'):
        ind_grow =1
        Ind_grow='Moderate(1% to 5%)'
    elif(ind_grow =='2'):
        Ind_grow='Good(>5% to 10%)'
        ind_grow =2
    elif(ind_grow =='3'):
        ind_grow =3
        Ind_grow='Strong(10%+)'
    else:
        ind_grow=0
        Ind_grow='No Growth(<1%)'

    mark_comp=request.POST['mark_comp']
    if (mark_comp == '1'):
        mark_comp = 1
        Mark_comp='Moderately Competitive'
    elif (mark_comp == '2'):
        mark_comp = 2
        Mark_comp='Dominant Player'
    else:
        mark_comp=0
        Mark_comp='Highly Competitive'

    barrier=request.POST['barrier']
    if (barrier == '1'):
        barrier = 1
        Barrier='Average'
    elif (barrier == '2'):
        Barrier = 'Difficult'
        barrier = 2
    else:
        barrier=0
        Barrier = 'Easy'
    totalB = sales + outlook + ind_grow + mark_comp + barrier
    ############### End of the first B ##################

    experience=request.POST['experience_m&m']
    if (experience == '5'):
        Experience='More than 10 years in the related line of business'
        experience = 5
    elif (experience == '2'):
        Experience = '1-5 years in the related line of business'
        experience = 2
    elif (experience == '3'):
        experience = 3
        Experience = '5-10 years in the related line of business'
    else:
        Experience = 'No experience'
        experience = 0

    succession = request.POST['succession']
    if (succession == '5'):
        succession = 5
        Succession='Ready Succession'
    elif (succession == '2'):
        Succession = 'Succession within 3-5 years'
        succession = 2
    elif (succession == '3'):
        succession = 3
        Succession = 'Succession within 2-3 years'
    else:
        succession = 0
        Succession = 'Succession in question'

    teamWork = request.POST['teamWork']
    if (teamWork == '5'):
        TeamWork='Very Good'
        teamWork = 5
    elif (teamWork == '2'):
        TeamWork = 'Poor'
        teamWork = 2
    elif (teamWork == '3'):
        teamWork = 3
        TeamWork = 'Moderate'
    else:
        teamWork = 0
        TeamWork = 'Regular Conflict'

    totalC =  experience + succession + teamWork

    ############### End of the first C ##################
    # print(request.POST['security'])
    # print(request.POST['collateral'])
    security = request.POST['security']
    if (security == '4'):
        security = 4
        Security='Fully pledged facilities /substantial cash covered'
    elif (security == '2'):
        Security = '2nd charge / inferrior charge'
        security = 2
    elif (security == '3'):
        security = 3
        Security = 'Registered Hypothecation (1st charge / 1st pari passu charge)'
    elif (security == '1'):
        security = 1
        Security = 'Simple Hypothecation/Negative Lien'
    else:
        Security = 'No security'
        security = 0

    collateral = request.POST['collateral']
    if (collateral == '4'):
        collateral = 4
        Collateral='Registered Mortage on Municipal Corporation/prime area property'
    elif (collateral == '2'):
        collateral = 2
        Collateral = 'Equitable Mortage or no property but plant and machinery as collateral'
    elif (collateral == '3'):
        collateral = 3
        Collateral = 'Registered Mortage on Pourashava/Semi urban area property'
    elif (collateral == '1'):
        collateral = 1
        Collateral = 'Negative lien on collateral'
    else:
        Collateral='No colleteral'
        collateral = 0

    guarantee=request.POST['guarantee']

    if (guarantee == '2'):
        guarantee = 2
        Guarantee="Personal Guarantee with high networth or Strong Corporate Guarantee(Guarantors' Grading Accecptable or Higher)"
    elif (guarantee == '1'):
        guarantee = 1
        Guarantee = 'Personal Guarantee or Corporate Guarantee with average financial strength'
    else:
        Guarantee = 'No support Guarantee'
        guarantee = 0

    totalD=security + collateral + guarantee

    ############### End of the first D ##################
    utilization = request.POST['utilization']
    if (utilization == '2'):
        utilization = 2
        Utilization='51% - 70%'
    elif (utilization == '3'):
        Utilization = 'More than 70%'
        utilization = 3
    elif (utilization == '1'):
        utilization = 1
        Utilization = '30% - 50%'
    else:
        utilization = 0
        Utilization = 'Less than 30%'

    conduct = request.POST['conduct']
    if (conduct == '2'):
        conduct = 2
        Conduct='Less than 3 years accounts with faultless record'
    elif (conduct == '3'):
        conduct = 3
        Conduct = 'More than 3 years accounts with faultless record'
    elif (conduct == '1'):
        conduct = 1
        Conduct = 'Accounts having satisfactory dealings with some late payments'
    else:
        conduct = 0
        Conduct = 'Frequent past dues & irregular dealings in account'

    conditions = request.POST['conditions']
    if (conditions == '2'):
        conditions = 2
        Conditions='Full Compliance'
    elif (conditions == '1'):
        Conditions = 'Some Non-Compliance'
        conditions = 1
    else:
        Conditions = 'No Compliance'
        conditions = 0
    # print(request.POST['deposits'])
    deposits = request.POST['deposits']
    if (deposits == '2'):
        deposits = 2
        Deposits='All personal accounts of the key business Sponsors/Pincipals are maintained in the FIs, with significant deposits'
    elif (deposits == '1'):
        deposits = 1
        Deposits = 'Principals maintain some accounts, but have relationship with other FIs'
    else:
        deposits = 0
        Deposits = 'No depository relationship'

    totalE = utilization + conditions + conduct + deposits
    ############### End of the first E ##################

    fullTotal= totalA + totalB + totalC + totalD + totalE

    if(fullTotal>=85):
        grade="Superior"
    elif(fullTotal>=75 and fullTotal <=84):
        grade="Good"
    elif (fullTotal >= 65 and fullTotal <=74 ):
        grade = "Acceptable"
    elif (fullTotal >= 55 and fullTotal <= 64):
        grade = "Marginal/Watchlist"
    elif (fullTotal >= 45 and fullTotal <= 54):
        grade = "Special Mention"
    elif (fullTotal >= 35 and fullTotal <= 44):
        grade = "Sub Standard"
    elif (fullTotal >= 25 and fullTotal <= 34):
        grade = "Doubtful"
    else:
        grade="Bad/Loss"

    print(grade)
    context={
        'ref':ref,
        'date':date,
        'borrower':borrower,
        'group':group,
        'sector':sector,
        'financial':financial,
        'completedby':completedby,
        'approvedby':approvedby,

        #end of details

        'debt':debt,
        'cur_rat':cur_rat,
        'opm':opm,
        'icr':icr,
        'totalA':totalA,
        # end of A
        'sales':sales,
        'outlook':outlook,
        'Outlook':Outlook,

        'ind_grow':ind_grow,
        'Ind_grow':Ind_grow,
        'mark_comp':mark_comp,
        'Mark_comp':Mark_comp,
        'barrier':barrier,
        'Barrier':Barrier,
        'totalB':totalB,
    #     end of B
        'experience': experience,
        'Experience': Experience,
        'Succession':Succession,
        'succession':succession,
        'TeamWork': TeamWork,
        'teamWork': teamWork,
        'totalC':totalC,
    #     end of C
        'security':security,
        'Security':Security,
        'collateral':collateral,
        'Collateral':Collateral,
        'guarantee':guarantee,
        'Guarantee':Guarantee,
        'totalD':totalD,
    #      end of D
        'utilization':utilization,
        'Utilization':Utilization,
        'Conduct':Conduct,
        'conduct':conduct,
        'conditions':conditions,
        'Conditions':Conditions,
        'deposits':deposits,
        'Deposits':Deposits,
        'totalE':totalE,

    #    end of E
        'fullTotal': fullTotal,
        'grade':grade,

    #     making actual parameter
        'Debt':Debt,
        'Cur_rat':Cur_rat,
        'Opm':Opm,
        'Icr':Icr,
        'Sales':Sales,


    }


    return render(request,'table.html',context)


def submission(request):
    return render(request,'table.html',{})