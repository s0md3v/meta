# -*- coding: utf-8 -*-
# Copyright JS Foundation and other contributors, https://js.foundation/
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import unicode_literals


class Token:
    BooleanLiteral = 1
    EOF = 2
    Identifier = 3
    Keyword = 4
    NullLiteral = 5
    NumericLiteral = 6
    Punctuator = 7
    StringLiteral = 8
    RegularExpression = 9
    Template = 10
    BigIntLiteral = 11
    PrivateIdentifier = 12


TokenName = {}
TokenName[Token.BooleanLiteral] = "Boolean"
TokenName[Token.EOF] = "<end>"
TokenName[Token.Identifier] = "Identifier"
TokenName[Token.Keyword] = "Keyword"
TokenName[Token.NullLiteral] = "Null"
TokenName[Token.NumericLiteral] = "Numeric"
TokenName[Token.Punctuator] = "Punctuator"
TokenName[Token.StringLiteral] = "String"
TokenName[Token.RegularExpression] = "RegularExpression"
TokenName[Token.Template] = "Template"
TokenName[Token.BigIntLiteral] = "BigInt"
TokenName[Token.PrivateIdentifier] = "PrivateIdentifier"
