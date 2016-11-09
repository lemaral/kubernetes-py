#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# This file is subject to the terms and conditions defined in
# file 'LICENSE.md', which is part of this source code package.
#

from kubernetes.K8sObject import K8sObject
from kubernetes.K8sContainer import K8sContainer


class K8sPodBasedObject(K8sObject):

    def __init__(self, name=None, obj_type=None, config=None):
        super(K8sPodBasedObject, self).__init__(config=config, obj_type=obj_type, name=name)

    # ------------------------------------------------------------------------------------- add

    # ------------------------------------------------------------------------------------- delete

    # ------------------------------------------------------------------------------------- get

    def get_pod_containers(self):
        return self.model.get_pod_containers()

    def get_pod_node_name(self):
        return self.model.get_pod_node_name()

    def get_pod_node_selector(self):
        return self.model.get_pod_node_selector()

    def get_pod_restart_policy(self):
        return self.model.get_pod_restart_policy()

    def get_service_account(self):
        return self.model.get_service_account()

    def get_termination_grace_period(self):
        return self.model.get_termination_grace_period()

    # ------------------------------------------------------------------------------------- set

    def set_active_deadline(self, seconds=None):
        self.model.set_active_deadline(seconds=seconds)
        return self

    def set_container_image(self, name, image=None):
        self.model.set_pod_image(name=name, image=image)
        return self

    def set_dns_policy(self, policy=None):
        self.model.set_dns_policy(policy=policy)
        return self

    def set_pod_generate_name(self, mode=None, name=None):
        self.model.set_pod_generate_name(mode=mode, name=name)
        return self

    def set_pod_node_name(self, name=None):
        self.model.set_pod_node_name(name=name)
        return self

    def set_pod_node_selector(self, selector=None):
        self.model.set_pod_node_selector(selector=selector)
        return self

    def set_pod_restart_policy(self, policy=None):
        self.model.set_pod_restart_policy(policy=policy)
        return self

    def set_service_account(self, name=None):
        self.model.set_service_account(name=name)
        return self

    def set_termination_grace_period(self, seconds=None):
        self.model.set_termination_grace_period(seconds=seconds)
        return self
