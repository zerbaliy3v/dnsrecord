import tcolor
import dns.resolver
import optparse
import time
# pip install -r requirements.txt


col = tcolor.Color()
dns_record_type: list = [
    'A','AAAA', 'ALIAS', 'CNAME', 'MX', 'NS', 'PTR', 'SOA', 'SRV', 'TXT', 'AFSDB', 'ANAME', 
    'SPF', 'HINFO', 'HIP', 'HTTPS', 'IPSECKEY', 'IXFR', 'KEY','KX', 'LOC', 'NAPTR', 'TLSA', 
    'OPT','NXT', 'TA', 'URI'
]
def banner():
    print(f"""{col.white}
     _                                      _ 
    | |                                    | |
  __| |_ __  ___ _ __ ___  ___ ___  _ __ __| |
 / _` | '_ \/ __| '__/ _ \/ __/ _ \| '__/ _` |
| (_| | | | \__ \ | |  __/ (_| (_) | | | (_| |
 \__,_|_| |_|___/_|  \___|\___\___/|_|  \__,_|
                                            {col.red}@zerbaliy3v {col.reset}                                   
""")

def argument():
    parser = optparse.OptionParser()
    parser.add_option('-d','--domain',dest='_domain',help='A target domain name')
    parser.add_option('-t','--type',dest='_type',help='ADD A DNS Recor type')
    (options, arguments) =  parser.parse_args()
    if not options._domain:
        parser.error('Help menu -h  or  --help')
    return options
domain = argument()._domain

def get_dns_record(domain: str) :
    resolver = dns.resolver.Resolver()
    
    if argument()._type:
        types = argument()._type
        dns_record_type.append(types)
        try:
            answers = resolver.resolve(domain, types)
            time.sleep(1)  
        except dns.resolver.NoAnswer:
            print("-"*100)
            print(f"❌ No {types} records for {domain}.{col.reset}")
        except dns.rdatatype.UnknownRdatatype:
            print("-"*100)
            print(f"👀{col.white} DNS resource record type is unknown [{types}]{col.reset}")
        except Exception as e :
            print('❗Error: \n',e)
        print("-"*100)
        print(f"✅{col.white} {types} records for {domain}:{col.reset}")
        for rdata in answers:
            print(f"- {col.blue} {rdata} {col.reset}") 
    else:
        for record_type in dns_record_type:
            try:
                answers = resolver.resolve(domain, record_type)
                time.sleep(1)  
            except dns.resolver.NoAnswer:
                print("-"*100)
                print(f"❌ No {record_type} records for {domain}.{col.reset}")
                continue
            except dns.rdatatype.UnknownRdatatype:
                print("-"*100)
                print(f"👀{col.white} DNS resource record type is unknown [{record_type}]{col.reset}")
                continue
            except Exception as e :
                print('❗Error: \n',e)
            print("-"*100)
            print(f"✅{col.white} {record_type} records for {domain}:{col.reset}")
            for rdata in answers:
                print(f"- {col.blue} {rdata} {col.reset}")

if __name__ == "__main__" :
    banner()
    try:
        get_dns_record(domain)
    except Exception as e:
        print(f"\n💁\n - {e}")
    




