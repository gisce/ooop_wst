# -*- coding: utf-8 -*-
import xmlrpclib

from ooop import OOOP


class OOOP_WST(OOOP):
    """Reimplementation to support ws_transactions module.
    """

    def __init__(self, user='admin', pwd='admin', dbname='openerp',
        uri='http://localhost', port=8069, debug=False, **kwargs):
        OOOP.__init__(self, user=user, pwd=pwd, dbname=dbname, uri=uri,
                       port=port, debug=debug, **kwargs)
        self.transaction_id = False
        self.transsock = xmlrpclib.ServerProxy('%s:%i/xmlrpc/ws_transaction'
                                               % (self.uri, self.port))

    def begin(self):
        self.transaction_id = self.transsock.begin(self.dbname, self.uid,
                                                   self.pwd)
        # Reloading modules for transaction
        self.load_models()
        return self.transaction_id

    def rollback(self):
        if self.transaction_id:
            return self.transsock.rollback(self.dbname, self.uid, self.pwd,
                                           self.transaction_id)
        return False

    def commit(self):
        if self.transaction_id:
            return self.transsock.commit(self.dbname, self.uid, self.pwd,
                                         self.transaction_id)
        return False

    def close(self):
        if self.transaction_id:
            self.transsock.close(self.dbname, self.uid, self.pwd,
                                 self.transaction_id)
            self.transaction_id = False
        return False

    def execute(self, model, *args):
        if self.transaction_id:
            return self.transsock.execute(self.dbname, self.uid, self.pwd,
                                          self.transaction_id, model, *args)
        else:
            return self.objectsock.execute(self.dbname, self.uid, self.pwd,
                                           model, *args)
