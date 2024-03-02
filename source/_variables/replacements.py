###############################################################################
#
# Custom replacements
#
# This file contains the dictionary of custom replacements. Requires the 
# variables 'version', 'release' and 'is_latest_release' from 
# source/_variables/settings.py
#

import sys
import os
sys.path.append(os.path.abspath("_variables"))
from settings import version, is_latest_release, release


custom_replacements = {
    # === URLs and base URLs
    "|CHECKSUMS_URL|" : "https://packages.fortishield.com/4.x/checksums/fortishield/",
    "|APK_CHECKSUMS_I386_URL|" : "alpine/x86",
    "|APK_CHECKSUMS_X86_64_URL|" : "alpine/x86_64",
    "|APK_CHECKSUMS_AARCH64_URL|" : "alpine/aarch64",
    "|APK_CHECKSUMS_ARMV7_URL|" : "alpine/armv7",
    "|APK_CHECKSUMS_ARMHF_URL|" : "alpine/armhf",
    "|APK_CHECKSUMS_PPC_URL|" : "alpine/ppc64le",
    "|APK_AGENT_I386_URL|" : "https://packages.fortishield.com/4.x/alpine/v3.12/main/x86/fortishield-agent",
    "|APK_AGENT_X86_64_URL|" : "https://packages.fortishield.com/4.x/alpine/v3.12/main/x86_64/fortishield-agent",
    "|APK_AGENT_AARCH64_URL|" : "https://packages.fortishield.com/4.x/alpine/v3.12/main/aarch64/fortishield-agent",
    "|APK_AGENT_ARMV7_URL|" : "https://packages.fortishield.com/4.x/alpine/v3.12/main/armv7/fortishield-agent",
    "|APK_AGENT_ARMHF_URL|" : "https://packages.fortishield.com/4.x/alpine/v3.12/main/armhf/fortishield-agent",
    "|APK_AGENT_PPC_URL|" : "https://packages.fortishield.com/4.x/alpine/v3.12/main/ppc64le/fortishield-agent",
    "|RPM_AGENT_URL|" : "https://packages.fortishield.com/4.x/yum/fortishield-agent",
    "|RPM_MANAGER_URL|" : "https://packages.fortishield.com/4.x/yum/fortishield-manager",
    "|DEB_AGENT_URL|" : "https://packages.fortishield.com/4.x/apt/pool/main/w/fortishield-agent/fortishield-agent",
    "|DEB_MANAGER_URL|" : "https://packages.fortishield.com/4.x/apt/pool/main/w/fortishield-manager/fortishield-manager",
    #
    "|CTI_URL|" : "https://cti.fortishield.com/api/v1/catalog/contexts/vd_1.0.0/consumers/vd_4.8.0",
    #
    # === Global and Fortishield version (fortishield agent, manager, indexer, and dashboard)
    "|FORTISHIELD_CURRENT_MAJOR|" : "4.x",
    "|FORTISHIELD_CURRENT_MINOR|" : version,
    "|FORTISHIELD_CURRENT|" : release,
    "|PYTHON_CLOUD_CONTAINERS_MIN|": "3.7",
    "|PYTHON_CLOUD_CONTAINERS_MAX|": "3.11",

    # --- Revision numbers for Fortishield agent and manager packages versions
    # Alpine APK packages revisions
    "|FORTISHIELD_REVISION_APK_AGENT_I386|" : "r1",
    "|FORTISHIELD_REVISION_APK_AGENT_X86_64|" : "r1",
    "|FORTISHIELD_REVISION_APK_AGENT_AARCH64|" : "r1",
    "|FORTISHIELD_REVISION_APK_AGENT_ARMV7|" : "r1",
    "|FORTISHIELD_REVISION_APK_AGENT_ARMHF|" : "r1",
    "|FORTISHIELD_REVISION_APK_AGENT_PPC|" : "r1",
    # Yum packages revisions
    "|FORTISHIELD_REVISION_YUM_AGENT_I386|" : "1",
    "|FORTISHIELD_REVISION_YUM_MANAGER_I386|" : "1",
    "|FORTISHIELD_REVISION_YUM_AGENT_I386_EL5|" : "1",
    #"|FORTISHIELD_REVISION_YUM_MANAGER_I386_EL5|" :
    "|FORTISHIELD_REVISION_YUM_AGENT_X86|" : "1",
    "|FORTISHIELD_REVISION_YUM_MANAGER_X86|" : "1",
    "|FORTISHIELD_REVISION_YUM_AGENT_X86_EL5|" : "1",
    #|FORTISHIELD_REVISION_YUM_MANAGER_X86_EL5|
    "|FORTISHIELD_REVISION_YUM_AGENT_AARCH64|" : "1",
    "|FORTISHIELD_REVISION_YUM_MANAGER_AARCH64|" : "1",
    "|FORTISHIELD_REVISION_YUM_AGENT_ARMHF|" : "1",
    #"|FORTISHIELD_REVISION_YUM_MANAGER_ARMHF|" : "1",
    "|FORTISHIELD_REVISION_YUM_AGENT_PPC|" : "1",
    #|FORTISHIELD_REVISION_YUM_MANAGER_PPC|" :
    # Deb packages revisions
    "|FORTISHIELD_REVISION_DEB_AGENT_I386|" : "1",
    "|FORTISHIELD_REVISION_DEB_MANAGER_I386|" : "1",
    "|FORTISHIELD_REVISION_DEB_AGENT_X86|" : "1",
    "|FORTISHIELD_REVISION_DEB_MANAGER_X86|" : "1",
    "|FORTISHIELD_REVISION_DEB_AGENT_AARCH64|" : "1",
    "|FORTISHIELD_REVISION_DEB_MANAGER_AARCH64|" : "1",
    "|FORTISHIELD_REVISION_DEB_AGENT_ARMHF|" : "1",
    "|FORTISHIELD_REVISION_DEB_MANAGER_ARMHF|" : "1",
    "|FORTISHIELD_REVISION_DEB_AGENT_PPC|" : "1",
    #"|FORTISHIELD_REVISION_DEB_MANAGER_PPC|" : 
    #
    # === Fortishield indexer version revisions
    "|FORTISHIELD_INDEXER_CURRENT_REV|" : "1", # RPM and Deb
    #"|FORTISHIELD_INDEXER_CURRENT_REV_DEB|" :
    # --- Architectures for Fortishield indexer packages
    "|FORTISHIELD_INDEXER_x64_RPM|" : "x86_64",
    "|FORTISHIELD_INDEXER_x64_DEB|" : "amd64",
    #
    # === Fortishield dashboard version revisions
    "|FORTISHIELD_DASHBOARD_CURRENT_REV_RPM|" : "1",
    "|FORTISHIELD_DASHBOARD_CURRENT_REV_DEB|" : "1",
    # --- Architectures for Fortishield dashboard packages
    "|FORTISHIELD_DASHBOARD_x64_RPM|" : "x86_64",
    "|FORTISHIELD_DASHBOARD_x64_DEB|" : "amd64",
    #
    # === Versions and revisions for other Fortishield deployments
    #"|FORTISHIELD_CURRENT_MAJOR_AMI|" :
    #"|FORTISHIELD_CURRENT_MINOR_AMI|" :
    "|FORTISHIELD_CURRENT_AMI|" : release,
    "|FORTISHIELD_CURRENT_MAJOR_OVA|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_OVA|" :
    "|FORTISHIELD_CURRENT_OVA|" : release,
    #"|FORTISHIELD_CURRENT_MAJOR_DOCKER|" :
    "|FORTISHIELD_CURRENT_MINOR_DOCKER|" : version,
    "|FORTISHIELD_CURRENT_DOCKER|" : release,
    #"|FORTISHIELD_CURRENT_MAJOR_KUBERNETES|" :
    #"|FORTISHIELD_CURRENT_MINOR_KUBERNETES|" :
    "|FORTISHIELD_CURRENT_KUBERNETES|" : release,
    #"|FORTISHIELD_CURRENT_MAJOR_ANSIBLE|" :
    "|FORTISHIELD_CURRENT_MINOR_ANSIBLE|" : version,
    "|FORTISHIELD_CURRENT_ANSIBLE|" : release,
    #"|FORTISHIELD_CURRENT_MAJOR_PUPPET|" :
    #"|FORTISHIELD_CURRENT_MINOR_PUPPET|" :
    "|FORTISHIELD_CURRENT_PUPPET|" : release,
    #"|FORTISHIELD_CURRENT_MAJOR_FROM_SOURCES|" :
    "|FORTISHIELD_CURRENT_MINOR_FROM_SOURCES|" : version,
    "|FORTISHIELD_CURRENT_FROM_SOURCES|" : release,
    #"|FORTISHIELD_CURRENT_MAJOR_WIN_FROM_SOURCES|" :
    #"|FORTISHIELD_CURRENT_MINOR_WIN_FROM_SOURCES|" :
    "|FORTISHIELD_CURRENT_WIN_FROM_SOURCES|" : release,
    "|FORTISHIELD_CURRENT_WIN_FROM_SOURCES_REV|" : "1",
    #
    # === Versions and revisions for packages of specific operating systems
    "|FORTISHIELD_CURRENT_MAJOR_WINDOWS|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_WINDOWS|" :
    "|FORTISHIELD_CURRENT_WINDOWS|" : release,
    "|FORTISHIELD_REVISION_WINDOWS|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_OSX|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_OSX|" :
    "|FORTISHIELD_CURRENT_OSX|" : release,
    "|FORTISHIELD_REVISION_OSX|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_SOLARIS|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_SOLARIS|" :
    "|FORTISHIELD_CURRENT_SOLARIS|" : release, # Set here the lesser of FORTISHIELD_CURRENT_MAJOR_SOLARIS10 and 11 values
    #"|FORTISHIELD_REVISION_SOLARIS|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_SOLARIS10|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_SOLARIS10|" :
    "|FORTISHIELD_CURRENT_SOLARIS10|" : release,
    #"|FORTISHIELD_REVISION_SOLARIS10|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_SOLARIS11|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_SOLARIS11|" :
    "|FORTISHIELD_CURRENT_SOLARIS11|" : release,
    #"|FORTISHIELD_REVISION_SOLARIS11|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_SOLARIS10_i386|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_SOLARIS10_i386|" :
    "|FORTISHIELD_CURRENT_SOLARIS10_i386|" : release,
    #"|FORTISHIELD_REVISION_SOLARIS10_i386|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_SOLARIS10_SPARC|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_SOLARIS10_SPARC|" :
    "|FORTISHIELD_CURRENT_SOLARIS10_SPARC|" : release,
    #"|FORTISHIELD_REVISION_SOLARIS10_SPARC|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_SOLARIS11_i386|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_SOLARIS11_i386|" :
    "|FORTISHIELD_CURRENT_SOLARIS11_i386|" : release,
    #"|FORTISHIELD_REVISION_SOLARIS11_i386|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_SOLARIS11_SPARC|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_SOLARIS11_SPARC|" :
    "|FORTISHIELD_CURRENT_SOLARIS11_SPARC|" : release,
    #"|FORTISHIELD_REVISION_SOLARIS11_SPARC|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_AIX|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_AIX|" :
    "|FORTISHIELD_CURRENT_AIX|" : release,
    "|FORTISHIELD_REVISION_AIX|" : "1",
    "|FORTISHIELD_CURRENT_MAJOR_HPUX|" : "4.x",
    #"|FORTISHIELD_CURRENT_MINOR_HPUX|" :
    "|FORTISHIELD_CURRENT_HPUX|" : release,
    "|FORTISHIELD_REVISION_HPUX|" : "1",
    #
    # === Elastic
    # --- Filebeat
    "|FILEBEAT_LATEST|" : "7.10.2",
    "|FILEBEAT_LATEST_AMI|" : "7.10.2",
    "|FILEBEAT_LATEST_OVA|" : "7.10.2",
    # --- Open Distro for Elasticsearch
    "|OPEN_DISTRO_LATEST|" : "1.13.2",
    # --- Elasticsearch
    "|ELASTICSEARCH_ELK_LATEST|" : "7.17.13", # Basic license
    "|ELASTICSEARCH_LATEST|" : "7.10.2",
    # --- Other Elastic
    "|ELASTIC_6_LATEST|" : "6.8.8",
    #
    # === Splunk
    "|SPLUNK_LATEST|" : "8.2.8",
    "|FORTISHIELD_SPLUNK_CURRENT|" : release,
    #
    "|SPLUNK_LATEST_MINOR|" : "8.2",
    "|FORTISHIELD_SPLUNK_REV_CURRENT_LATEST|" : "1", # 8.2
    "|FORTISHIELD_SPLUNK_REV_CURRENT_8.1|" : "1",
}

if is_latest_release:
    custom_replacements["|FORTISHIELD_INDEXER_RPM_PKG_INSTALL|"] = ''
    custom_replacements["|FORTISHIELD_MANAGER_RPM_PKG_INSTALL|"] = ''
    custom_replacements["|FORTISHIELD_DASHBOARD_RPM_PKG_INSTALL|"] = ''
    custom_replacements["|FORTISHIELD_INDEXER_DEB_PKG_INSTALL|"] = ''
    custom_replacements["|FORTISHIELD_MANAGER_DEB_PKG_INSTALL|"] = ''
    custom_replacements["|FORTISHIELD_DASHBOARD_DEB_PKG_INSTALL|"] = ''
    custom_replacements["|FORTISHIELD_AGENT_RPM_PKG_INSTALL|"] = ''
    custom_replacements["|FORTISHIELD_AGENT_DEB_PKG_INSTALL|"] = ''
    custom_replacements["|FORTISHIELD_AGENT_ZYPP_PKG_INSTALL|"] = ''
    custom_replacements["|FORTISHIELD_AGENT_APK_PKG_INSTALL|"] = ''
else:
    custom_replacements["|FORTISHIELD_INDEXER_RPM_PKG_INSTALL|"] = '-' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + custom_replacements["|FORTISHIELD_INDEXER_CURRENT_REV|"]
    custom_replacements["|FORTISHIELD_MANAGER_RPM_PKG_INSTALL|"] = '-' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + custom_replacements["|FORTISHIELD_REVISION_YUM_MANAGER_X86|"]
    custom_replacements["|FORTISHIELD_DASHBOARD_RPM_PKG_INSTALL|"] = '-' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + custom_replacements["|FORTISHIELD_DASHBOARD_CURRENT_REV_RPM|"]
    custom_replacements["|FORTISHIELD_INDEXER_DEB_PKG_INSTALL|"] = '=' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + custom_replacements["|FORTISHIELD_INDEXER_CURRENT_REV|"]
    custom_replacements["|FORTISHIELD_MANAGER_DEB_PKG_INSTALL|"] = '=' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + custom_replacements["|FORTISHIELD_REVISION_DEB_MANAGER_X86|"]
    custom_replacements["|FORTISHIELD_DASHBOARD_DEB_PKG_INSTALL|"] = '=' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + custom_replacements["|FORTISHIELD_DASHBOARD_CURRENT_REV_DEB|"]
    custom_replacements["|FORTISHIELD_AGENT_RPM_PKG_INSTALL|"] = '-' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + custom_replacements["|FORTISHIELD_REVISION_YUM_AGENT_X86|"]
    custom_replacements["|FORTISHIELD_AGENT_DEB_PKG_INSTALL|"] = '=' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + custom_replacements["|FORTISHIELD_REVISION_DEB_AGENT_X86|"]
    custom_replacements["|FORTISHIELD_AGENT_ZYPP_PKG_INSTALL|"] = '-' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + '1'
    custom_replacements["|FORTISHIELD_AGENT_APK_PKG_INSTALL|"] = '=' + custom_replacements["|FORTISHIELD_CURRENT|"] + '-' + custom_replacements["|FORTISHIELD_REVISION_APK_AGENT_X86_64|"]
