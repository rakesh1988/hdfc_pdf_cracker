
### hacked a script to decrypt the customer id of a HDFC bank statement. 

I have been receiving statements from HDFC which does not belong to me. I have contacted HDFC customer care multiple times and they didn't care. Hence thought of decrypting and notifying the account holder.

### usage
* install PyPDF2 as follows
    * pip intall --user PyPDF2
* I ran this as a background process as follows
    * nohup python -u hdfc_pdf_cracker.py --file hdfc.pdf > hdfc_pdf_cracker.log &