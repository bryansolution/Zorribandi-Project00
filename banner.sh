#!/data/data/com.termux/files/usr/bin/bash
# Banner Pro para Zorribandi 🦨🛡️

clear
echo -e "\e[1;33m  __________________________________________________"
echo -e "\e[1;33m /                                                  \\"
echo -e "\e[1;32m |  \e[1;37m🦊 ZORRIBANDI SECURITY LAB \e[1;33m- \e[1;32mPROJECT-00 \e[1;33m     |"
echo -e "\e[1;33m |  \e[1;34m---------------------------------------------- \e[1;33m |"
echo -e "\e[1;33m |  \e[1;37mRESEARCHER: \e[1;36mZorribandi \e[1;33m                        |"
echo -e "\e[1;33m |  \e[1;37mENVIRONMENT: \e[1;35mTermux Android \e[1;33m                   |"
echo -e "\e[1;33m |  \e[1;37mSTATUS: \e[1;32mActive \e[1;31m🦨🛡️ \e[1;33m                                |"
echo -e "\e[1;33m \\__________________________________________________/\e[0m"
echo ""
echo -e "\e[1;37m[i] Hoy es: \e[1;32m$(date +'%D %T')\e[0m"
echo -e "\e[1;37m[i] IP Local: \e[1;34m$(ifconfig | grep -oE 'inet [0-9.]+' | grep -v '127.0.0.1' | cut -d' ' -f2)\e[0m"
echo ""


