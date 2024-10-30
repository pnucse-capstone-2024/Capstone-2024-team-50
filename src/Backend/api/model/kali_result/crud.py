from datetime import datetime
from sqlalchemy.orm import Session, joinedload

from sqlalchemy import and_

from typing import List

from . import models, schemas

def get_kali_host(db: Session, id: int):
    return db.query(models.KaliHost).filter(models.KaliHost.id == id).first()

def get_kali_host_by_ip_and_uid(db: Session, ip: str, uid: int):
    return db.query(models.KaliHost).filter(models.KaliHost.ip == ip, models.KaliHost.uid == uid).first()

def get_kali_hosts_by_uid(db: Session, uid: int):
    return db.query(models.KaliHost).filter(models.KaliHost.uid == uid).all()

def create_kali_host(db: Session, kali_host: schemas.KaliHostCreate):
    db_kali_host = models.KaliHost(os=kali_host.os, ip=kali_host.ip, uid=kali_host.uid)
    db.add(db_kali_host)
    db.commit()
    db.refresh(db_kali_host)
    return db_kali_host

def delete_kali_host(db: Session, id: int):
    # kali_products = db.query(models.KaliProduct).join(models.KaliHostService).join(models.KaliHost).filter(models.KaliHost.id == id).all()
    # if kali_products:
    #     for kp in kali_products:
    #         db.query(models.KaliProduct).filter(models.KaliProduct.id == kp.id).delete()

    # vulnerability = db.query(models.Vulnerability).join(models.KaliHostService).join(models.KaliHost).filter(models.KaliHost.id == id).all()
    # if vulnerability:
    #     for v in vulnerability:
    #         db.query(models.Vulnerability).filter(models.Vulnerability.id == v.id).delete()
            
    kali_host_services = db.query(models.KaliHostService).filter(models.KaliHostService.kali_host_id == id).all()
    if kali_host_services:
        for kali_host_service in kali_host_services:
            kali_products = db.query(models.KaliProduct).filter(models.KaliProduct.kali_host_service_id == kali_host_service.id).all()
            if kali_products:
                for kp in kali_products:
                    db.query(models.KaliProduct).filter(models.KaliProduct.id == kp.id).delete()
            vulnerabilities = db.query(models.Vulnerability).filter(models.Vulnerability.kali_host_service_id == kali_host_service.id).all()
            if vulnerabilities:
                for v in vulnerabilities:
                    db.query(models.Vulnerability).filter(models.Vulnerability.id == v.id).delete()
            db.query(models.Vulnerability).filter(models.Vulnerability.kali_host_service_id == kali_host_service.id).delete()
    db.query(models.KaliHost).filter(models.KaliHost.id == id).delete()
    db.commit()

def update_kali_host(db: Session, id: int, kali_host: schemas.KaliHostUpdate):
    db_kali_host = db.query(models.KaliHost).filter(models.KaliHost.id == id).first()
    db_kali_host.os = kali_host.os
    db_kali_host.ip = kali_host.ip
    db.commit()
    db.refresh(db_kali_host)
    return db_kali_host

def get_kali_host_service(db: Session, id: int):
    return db.query(models.KaliHostService).filter(models.KaliHostService.id == id).first()

def get_kali_host_services_by_kali_host_id(db: Session, kali_host_id: int):
    return db.query(models.KaliHostService).filter(models.KaliHostService.kali_host_id == kali_host_id).all()

def get_kali_host_services_by_uid(db: Session, uid: int):
    return db.query(models.KaliHostService).join(models.KaliHost).filter(models.KaliHost.uid == uid).all()

def create_kali_host_service(db: Session, kali_host_service: schemas.KaliHostServiceCreate, kali_host_id: int):
    db_kali_host_service = models.KaliHostService(service=kali_host_service.service, port=kali_host_service.port, kali_host_id=kali_host_id)
    db.add(db_kali_host_service)
    db.commit()
    db.refresh(db_kali_host_service)
    return db_kali_host_service

def delete_kali_host_service(db: Session, id: int):
    db.query(models.KaliProduct).filter(models.KaliProduct.kali_host_service_id == id).delete()
    db.query(models.Vulnerability).filter(models.Vulnerability.kali_host_service_id == id).delete()
    db.query(models.KaliHostService).filter(models.KaliHostService.id == id).delete()
    db.commit()

def delete_kali_host_service_by_service_and_kali_host_id(db: Session, service: str, kali_host_id: int):
    db.query(models.Vulnerability).join(models.KaliHostService).join(models.KaliHost).filter(and_(models.KaliHostService.service == service, models.KaliHost.id == kali_host_id)).delete()
    db.query(models.KaliHostService).join(models.KaliHost).filter(and_(models.KaliHostService.service == service, models.KaliHost.id == kali_host_id)).delete()
    db.commit()

def update_kali_host_service(db: Session, id: int, kali_host_service: schemas.KaliHostServiceUpdate):
    db_kali_host_service = db.query(models.KaliHostService).filter(models.KaliHostService.id == id).first()
    db_kali_host_service.service = kali_host_service.service
    db_kali_host_service.port = kali_host_service.port
    db_kali_host_service.banner = kali_host_service.banner
    db.commit()
    db.refresh(db_kali_host_service)
    return db_kali_host_service

def get_kali_product(db: Session, id: int):
    return db.query(models.KaliProduct).filter(models.KaliProduct.id == id).first()

def get_kali_products_by_kali_host_service_id(db: Session, kali_host_service_id: int):
    return db.query(models.KaliProduct).filter(models.KaliProduct.kali_host_service_id == kali_host_service_id).all()

def create_kali_product(db: Session, kali_product: schemas.KaliProductCreate, kali_host_service_id: int):
    db_kali_product = models.KaliProduct(type=kali_product.type, name=kali_product.name, version=kali_product.version, vendor=kali_product.vendor, kali_host_service_id=kali_host_service_id)
    db.add(db_kali_product)
    db.commit()
    db.refresh(db_kali_product)
    return db_kali_product

def delete_kali_product(db: Session, id: int):
    db.query(models.KaliProduct).filter(models.KaliProduct.id == id).delete()
    db.commit()

def get_vulnerability(db: Session, id: int):
    return db.query(models.Vulnerability).filter(models.Vulnerability.id == id).first()

def get_vulnerabilities_by_kali_host_service_id(db: Session, kali_host_service_id: int):
    return db.query(models.Vulnerability).filter(models.Vulnerability.kali_host_service_id == kali_host_service_id).all()

def create_vulnerability(db: Session, vulnerability: schemas.VulnerabilityCreate, kali_host_service_id: int):
    db_vulnerability = models.Vulnerability(name=vulnerability.name, cvss=vulnerability.cvss, title=vulnerability.title, description=vulnerability.description, url=vulnerability.url, type=vulnerability.type, kali_host_service_id=kali_host_service_id)
    db.add(db_vulnerability)
    db.commit()
    db.refresh(db_vulnerability)
    return db_vulnerability

def delete_vulnerability(db: Session, id: int):
    db.query(models.Vulnerability).filter(models.Vulnerability.id == id).delete()
    db.commit()