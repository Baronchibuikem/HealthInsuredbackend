from rest_framework import viewsets, status, mixins
from django.db.models import Sum
from app_claims.models import Payment, Claim
from app_claims.Api.Api_version_1.serializers.payment_serializer import ( AcceptPaymentSerializer, 
                                                RejectPaymentSerializer,CustomManager)
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

class AcceptPaymentView(viewsets.ModelViewSet):
    '''
    For approving a payment batch
    '''
    #queryset = Payment.objects.filter(is_approved=False)
    serializer_class = AcceptPaymentSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = (permissions.AllowAny,)
    name = "accept_batch_payment"

    def get_queryset(self, *args, **kwargs):
        """
        This method will display a the id of a payment batch, reason the payment was approved
        or rejected

        First we filter and get all unapproved batch, we then iterate over it and use the payment
        batch id to filter out claims in a batch and sum up the total amount_to_pay values

        For every iteration we append the value to customList and which we pass it into our
        AcceptPaymentSerializer which then return the data in json format
        """
        customList = []
        unapproved_payments = Payment.objects.all().order_by('id')
        for payment in unapproved_payments:
            total_amount = Claim.objects.filter(claim_batch=payment.batch.id).aggregate(Sum('amount_to_pay'))
            total_claims = Claim.objects.filter(claim_batch=payment.batch.id)
            vetted_claims = Claim.objects.filter(completed=True, claim_batch=payment.batch.id)
            #print(vetted_claims)
            customList.append(CustomManager(id=payment.id,
                reason_approved_or_denied=payment.reason_approved_or_denied, 
                total_approved = total_amount["amount_to_pay__sum"],
                batch = payment.batch,
                batch_id = payment.batch,
                is_approved = payment.is_approved,
                date_created = payment.date_created,
                vetted_claims = len(vetted_claims),
                total_claims = len(total_claims)
                ))
        serializer=self.serializer_class(customList,many=True)
        return customList

    def retrieve(self,request,pk):
        """
        This method is used to restrieve individual batch claims
        """
        unapproved_payment = Payment.objects.get(is_approved=False,pk=pk)
        total_amount = Claim.objects.filter(claim_batch=unapproved_payment.batch.id).aggregate(Sum('amount_to_pay'))
        vetted_claims = Claim.objects.filter(completed=True, claim_batch=unapproved_payment.id)
        total_claims = Claim.objects.filter(claim_batch=unapproved_payment.batch.id)
        print(len(vetted_claims))
            
        data=CustomManager(id=unapproved_payment.id,
            reason_approved_or_denied=unapproved_payment.reason_approved_or_denied, 
            total_approved = total_amount["amount_to_pay__sum"],
            batch = unapproved_payment.batch,
            batch_id = unapproved_payment.batch,
            is_approved = unapproved_payment.is_approved,
            date_created = unapproved_payment.date_created,
            vetted_claims = len(vetted_claims),
            total_claims = len(total_claims)
        )
        return Response(AcceptPaymentSerializer(data).data)

    def update(self,request,pk):
        instance=Payment.objects.get(pk=pk)
        instance.reason_approved_or_denied = request.data['reason_approved_or_denied']
        instance.save()
        return Response(AcceptPaymentSerializer(instance).data)

class RejectPaymentView(viewsets.ModelViewSet):
    """
    For rejecting a payment batch
    """
    queryset = Payment.objects.filter(is_approved=False)
    serializer_class = RejectPaymentSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    name = "reject_batch_payment"

