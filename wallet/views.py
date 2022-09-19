from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from numpy import rec
from .models import Details
from bitcoin import *
# import bs4
# import requests
from web3 import Web3
import random
from django.template.response import TemplateResponse


# Create your views here.
def index(request):

    if request.method == 'POST':
        detail = Details()
        # detail.sender_address = request.POST['sender_address']
        # detail.sender_private_key = request.POST['sender_private_key']
        # detail.receiver_address = request.POST['receiver_address']
        # detail.balance = request.POST['amount']
        sender_address = request.POST['sender_address']
        sender_private_key = request.POST['sender_private_key']
        receiver_address = request.POST['receiver_address']
        balance = request.POST['amount']
        Details.objects.create(sender_address=detail.sender_address, sender_private_key=detail.sender_private_key, receiver_address=detail.receiver_address, balance=detail.balance)
        # detail.save()
        # list1 = [sender_address, receiver_address,balance]
        list1 = 'Test value'
        ganache_url = # Enter Ganache URL #
        web3 = Web3(Web3.HTTPProvider(ganache_url))
        recv_addr = receiver_address

        sender_addr = sender_address
        sender_priv_key = sender_private_key

        print(web3.isConnected())

        nonce = web3.eth.getTransactionCount(sender_addr)

        tx = {
            'nonce': nonce,
            'to': recv_addr,
            'value': web3.toWei(balance, 'ether'), 
            'gas': 21000,
            'gasPrice': web3.toWei('50', 'gwei')
        }

        signed_tx = web3.eth.account.sign_transaction(tx, sender_priv_key)

        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        args = {}

        balance = web3.eth.get_balance(sender_address)

        t_hash = web3.toHex(tx_hash)

        print("Transaction Hash: ", t_hash)
        print("Block Numbers: ", web3.eth.block_number)

        bal = web3.fromWei(balance, 'ether')

        args["bal"] = bal
        args["t_hash"] = t_hash
        args["rec"] = receiver_address

        i = 0

        length_blockchains = web3.eth.block_number

        while i<= length_blockchains:
            block = web3.eth.get_block(i)

            for tx_hash in block['transactions']:
                tx = web3.eth.get_transaction(tx_hash)
                tx_obj = {'addr-sender': tx['from'], 'addr_receiver': tx['to'], 'value': tx['value']}

                print("Block Number: ", block['number'])
                print(tx_obj)
                print("Value: ", tx['value'])
                print(web3.toHex(tx_hash))
                print("Block Hash: ", web3.toHex(block['hash']))
                # print("Tx Hash: ", (web3.toHex(block['transactions'])))
                print("Block Parent Hash: ", web3.toHex(block['parentHash']), "\n")

            i += 1
        return TemplateResponse(request, 'index.htm', args)
   
    return render(request, 'index.htm')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')

    else:
        return render(request, 'login.htm')

def register(request):

    detail = Details()
    addr = { # Ganache Wallet Address and Private Key Pair #
    }
    
    address = random.choice(list(addr.keys()))
    private_key = addr[address]
    public_key = privtopub(private_key)
    detail.private_key = private_key
    detail.public_key = public_key
    detail.address = address


    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        private_key = request.POST['private_key']
        public_key = request.POST['public_key']
        address = request.POST['address']

        if password==password2:       
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, last_name=private_key, first_name=address)
                user.save();
                print('User Created')
                return redirect('login')

        else:
            messages.info(request, 'Password Not Matching')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.htm', {'detail': detail})

def logout(request):
    auth.logout(request)
    return redirect('/')